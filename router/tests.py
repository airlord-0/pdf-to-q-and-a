import json
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class AnswerEndpointTests(TestCase):
    def test_home_page_includes_the_answer_display(self):
        response = self.client.get("/")

        self.assertContains(response, 'id="answer"')
        self.assertContains(response, "answerElement.textContent = data.answer")

    def test_returns_llm_answer_as_json(self):
        with patch("router.views.generate_answer", return_value="Generated answer"):
            response = self.client.post(
                reverse("answer"),
                data=json.dumps({"question": "What is in the PDF?"}),
                content_type="application/json",
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"answer": "Generated answer"})

    def test_rejects_empty_questions(self):
        response = self.client.post(
            reverse("answer"), data=json.dumps({"question": "  "}), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Please enter a question.")

    def test_returns_json_error_when_llm_fails(self):
        with patch("router.views.generate_answer", side_effect=RuntimeError("provider unavailable")):
            response = self.client.post(
                reverse("answer"),
                data=json.dumps({"question": "What is in the PDF?"}),
                content_type="application/json",
            )

        self.assertEqual(response.status_code, 502)
        self.assertIn("Unable to generate", response.json()["error"])
