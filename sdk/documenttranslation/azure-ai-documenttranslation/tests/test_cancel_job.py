# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import functools
from testcase import DocumentTranslationTest
from preparer import DocumentTranslationPreparer, DocumentTranslationClientPreparer as _DocumentTranslationClientPreparer
from azure.ai.documenttranslation import DocumentTranslationClient, DocumentTranslationInput, TranslationTarget
DocumentTranslationClientPreparer = functools.partial(_DocumentTranslationClientPreparer, DocumentTranslationClient)


class TestCancelJob(DocumentTranslationTest):

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    def test_list_statuses(self, client):
        # prepare containers and test data
        blob_data = [b'This is some text']
        source_container_sas_url = self.create_source_container(data=blob_data)
        target_container_sas_url = self.create_target_container()

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[
                    TranslationTarget(
                        target_url=target_container_sas_url,
                        language_code="es"
                    )
                ]
            )
        ]

        # submit job
        job_details = client.create_translation_job(translation_inputs)
        self.assertIsNotNone(job_details.id)

        # cancel job
        client.cancel_job(job_details.id)
        self.wait(duration=10)  # for 'cancelled' status to propagate

        # check job status
        job_details = client.get_job_status(job_details.id)
        self._validate_translation_job(job_details, 1, "Cancelled")