import unittest
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from secureragpipeline.app import inngest_app
from secureragpipeline.config import DEFAULT_DEMO_TENANT_ID, DEFAULT_DEMO_USER_ROLE
from secureragpipeline.models.results import QueryAPIResponse, QueryRetrievalTrace


class QueryAPIEndpointTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(inngest_app.app)

    def test_query_endpoint_returns_success_response(self):
        response_model = QueryAPIResponse(
            answer="Document owner is Alice.",
            answer_decision="allow",
            role="employee",
            tenant_id="demo",
            retrieved_count=1,
            excluded_count=0,
            retrieval_trace=QueryRetrievalTrace(),
            output_filter_reasons=[],
        )

        with patch.object(inngest_app, "run_api_query", new=AsyncMock(return_value=response_model)):
            response = self.client.post(
                "/api/query",
                json={"question": "Who owns the document?", "role": "employee", "tenant_id": "demo"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["answer"], "Document owner is Alice.")

    def test_query_endpoint_requires_question(self):
        response = self.client.post("/api/query", json={"role": "employee", "tenant_id": "demo"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "question is required"})

    def test_query_endpoint_uses_default_role_and_tenant(self):
        response_model = QueryAPIResponse(
            answer="ok",
            answer_decision="allow",
            role=DEFAULT_DEMO_USER_ROLE,
            tenant_id=DEFAULT_DEMO_TENANT_ID,
            retrieved_count=0,
            excluded_count=0,
            retrieval_trace=QueryRetrievalTrace(),
            output_filter_reasons=[],
        )

        with patch.object(inngest_app, "run_api_query", new=AsyncMock(return_value=response_model)) as mocked_run:
            response = self.client.post(
                "/api/query",
                json={"question": "What is in the file?", "source_id": None},
            )

        self.assertEqual(response.status_code, 200)
        mocked_run.assert_awaited_once_with(
            question="What is in the file?",
            user_role=DEFAULT_DEMO_USER_ROLE,
            tenant_id=DEFAULT_DEMO_TENANT_ID,
            source_id=None,
        )

    def test_query_endpoint_response_contains_required_fields(self):
        response_model = QueryAPIResponse(
            answer="ok",
            answer_decision="allow",
            role="employee",
            tenant_id="demo",
            retrieved_count=1,
            excluded_count=1,
            retrieval_trace=QueryRetrievalTrace(),
            output_filter_reasons=[],
        )

        with patch.object(inngest_app, "run_api_query", new=AsyncMock(return_value=response_model)):
            response = self.client.post("/api/query", json={"question": "Who owns the document?"})

        self.assertEqual(response.status_code, 200)
        body = response.json()
        for field in (
            "answer",
            "answer_decision",
            "role",
            "tenant_id",
            "retrieved_count",
            "excluded_count",
            "retrieval_trace",
            "output_filter_reasons",
        ):
            self.assertIn(field, body)
