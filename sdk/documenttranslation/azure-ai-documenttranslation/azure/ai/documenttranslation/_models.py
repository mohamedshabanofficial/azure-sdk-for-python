# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import Any, List

from ._generated.models import (
    BatchRequest as _BatchRequest,
    SourceInput as _SourceInput,
    DocumentFilter as _DocumentFilter,
    TargetInput as _TargetInput,
    Glossary as _Glossary
)


class TranslationGlossary(object):
    """Glossary / translation memory for the request.

    :param glossary_url: Required. Location of the glossary.
     We will use the file extension to extract the formatting if the format parameter is not
     supplied.
     If the translation language pair is not present in the glossary, it will not be applied.
    :type glossary_url: str
    :keyword str format: Format.
    :keyword str format_version: Format version.
    :keyword storage_source: Storage Source. Default value: "AzureBlob".
    :paramtype storage_source: str
    """

    def __init__(
            self,
            glossary_url,
            **kwargs
    ):
        # type: (str, **Any) -> None
        self.glossary_url = glossary_url
        self.format = kwargs.get("format", None)
        self.format_version = kwargs.get("format_version", None)
        self.storage_source = kwargs.get("storage_source", None)

    @classmethod
    def _to_generated_list(cls, glossaries):
        result = list(_Glossary)
        for glossary in glossaries:
            if isinstance(TranslationGlossary):
                result.append(
                    _Glossary(
                        glossary_url = glossary.glossary_url,
                        format = glossary.format,
                        version = glossary.version,
                        storage_source = glossary.storage_source
                    )
                )
            elif isinstance(str):
                result.append(
                    _Glossary(
                        glossary_url = glossary,
                    )
                )
        return result


class StorageTarget(object):
    """Destination for the finished translated documents.

    :param target_url: Required. Location of the folder / container with your documents.
    :type target_url: str
    :param language: Required. Target Language.
    :type language: str
    :keyword str category_id: Category / custom system for translation request.
    :keyword glossaries: List of TranslationGlossary.
    :paramtype glossaries: Union[list[str], list[~azure.ai.documenttranslation.TranslationGlossary]]
    :keyword storage_source: Storage Source. Default value: "AzureBlob".
    :paramtype storage_source: str
    """

    def __init__(
        self,
        target_url,
        language,
        **kwargs
    ):
        # type: (str, str, **Any) -> None
        self.target_url = target_url
        self.language = language
        self.category_id = kwargs.get("category_id", None)
        self.glossaries = kwargs.get("glossaries", None)
        self.storage_source = kwargs.get("storage_source", None)

    @classmethod
    def _to_generated_list(cls, targets):
        return [
            _TargetInput(
                target_url = target.target_url,
                category = target.category_id,
                language = target.language,
                storage_source = target.storage_source,
                glossaries = TranslationGlossary._to_generated_list(target.glossaries)
            ) 
            for target in targets
        ]


class BatchDocumentInput(object):
    """Definition for the input batch translation request.

    :param source_url: Required. Location of the folder / container or single file with your
     documents.
    :type source_url: str
    :param targets: Required. Location of the destination for the output.
    :type targets: list[StorageTarget]
    :keyword str source_language: Language code
     If none is specified, we will perform auto detect on the document.
    :keyword str prefix: A case-sensitive prefix string to filter documents in the source path for
     translation. For example, when using a Azure storage blob Uri, use the prefix to restrict sub folders for
     translation.
    :keyword str suffix: A case-sensitive suffix string to filter documents in the source path for
     translation. This is most often use for file extensions.
    :keyword storage_type: Storage type of the input documents source string. Possible values
     include: "Folder", "File".
    :paramtype storage_type: str or ~azure.ai.documenttranslation.StorageInputType
    :keyword str storage_source: Storage Source. Default value: "AzureBlob".
    """

    def __init__(
        self,
        source_url,
        targets,
        **kwargs
    ):
        # type: (str, List[StorageTarget], **Any) -> None
        self.source_url = source_url
        self.targets = targets
        self.source_language = kwargs.get("source_language", None)
        self.storage_type = kwargs.get("storage_type", None)
        self.storage_source = kwargs.get("storage_source", None)
        self.prefix = kwargs.get("prefix", None)
        self.suffix = kwargs.get("suffix", None)

    @classmethod
    def _to_generated_list(cls, batch_document_inputs):
        return [
            _BatchRequest(
                source = _SourceInput(
                    source_url = batch_document_input.source_url,
                    filter = _DocumentFilter(
                        prefix = batch_document_input.prefix,
                        suffix = batch_document_input.suffix
                    ),
                    language = batch_document_input.source_language,
                    storage_source = batch_document_input.storage_source
                ),
                targets = StorageTarget._to_generated_list(batch_document_input.targets),
                storage_type = batch_document_input.storage_type
            )
            for batch_document_input in batch_document_inputs
        ]



class JobStatusDetail(object):
    """Job status response.

    :ivar id: Required. Id of the job.
    :vartype id: str
    :ivar created_on: Required. Operation created date time.
    :vartype created_on: ~datetime.datetime
    :ivar last_updated_on: Required. Date time in which the operation's status has been
     updated.
    :vartype last_updated_on: ~datetime.datetime
    :ivar status: Required. List of possible statuses for job or document. Possible values
     include: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling",
     "ValidationFailed".
    :vartype status: str
    :ivar error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :vartype error: ~azure.ai.documenttranslation.DocumentTranslationError
    :ivar int documents_total_count: Total count.
    :ivar int documents_failed_count: Failed count.
    :ivar int documents_succeeded_count: Number of Success.
    :ivar int documents_in_progress_count: Number of in progress.
    :ivar int documents_not_yet_started_count: Count of not yet started.
    :ivar int documents_cancelled_count: Number of cancelled.
    :ivar int total_characters_charged: Required. Total characters charged by the API.

    """

    def __init__(
        self,
        **kwargs
    ):
        # type: (**Any) -> None
        self.id = kwargs['id']
        self.created_on = kwargs['created_on']
        self.last_updated_on = kwargs['last_updated_on']
        self.status = kwargs.get('status', None)
        self.error = kwargs.get("error", None)
        self.documents_total_count = kwargs.get('documents_total_count', None)
        self.documents_failed_count = kwargs.get('documents_failed_count', None)
        self.documents_succeeded_count = kwargs.get('documents_succeeded_count', None)
        self.documents_in_progress_count = kwargs.get('documents_in_progress_count', None)
        self.documents_not_yet_started_count = kwargs.get('documents_not_yet_started_count', None)
        self.documents_cancelled_count = kwargs.get('documents_cancelled_count', None)
        self.total_characters_charged = kwargs.get('total_characters_charged', None)

    @classmethod
    def _from_generated(cls, batch_status_details):
        return cls(
            id = batch_status_details.id,
            created_on = batch_status_details.created_date_time_utc,
            last_updated_on = batch_status_details.last_action_date_time_utc,
            status = batch_status_details.status,
            error = DocumentTranslationError._from_generated(batch_status_details.error),
            documents_total_count = batch_status_details.summary.total,
            documents_failed_count = batch_status_details.summary.failed,
            documents_succeeded_count = batch_status_details.summary.success,
            documents_in_progress_count = batch_status_details.summary.in_progress,
            documents_not_yet_started_count = batch_status_details.summary.not_yet_started,
            documents_cancelled_count = batch_status_details.summary.cancelled,
            total_characters_charged = batch_status_details.summary.total_character_charged
        )


class DocumentStatusDetail(object):
    """DocumentStatusDetail.

    :ivar url: Required. Location of the document or folder.
    :vartype url: str
    :ivar created_on: Required. Operation created date time.
    :vartype created_on: ~datetime.datetime
    :ivar last_updated_on: Required. Date time in which the operation's status has been
     updated.
    :vartype last_updated_on: ~datetime.datetime
    :ivar status: Required. List of possible statuses for job or document. Possible values
     include: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling",
     "ValidationFailed".
    :vartype status: str
    :ivar translate_to: Required. To language.
    :vartype translate_to: str
    :ivar error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :vartype error: ~azure.ai.documenttranslation.DocumentTranslationError
    :ivar translation_progress: Progress of the translation if available.
    :vartype translation_progress: float
    :ivar id: Document Id.
    :vartype id: str
    :ivar int characters_charged: Character charged by the API.
    """

    def __init__(
        self,
        **kwargs
    ):
        # type: (**Any) -> None
        self.url = kwargs['url']
        self.created_on = kwargs['created_on']
        self.last_updated_on = kwargs['last_updated_on']
        self.status = kwargs['status']
        self.translate_to = kwargs['translate_to']
        self.error = kwargs.get('error', None)
        self.translation_progress = kwargs.get('translation_progress', None)
        self.id = kwargs.get('id', None)
        self.characters_charged = kwargs.get('characters_charged', None)


class DocumentTranslationError(object):
    """This contains an outer error with error code, message, details, target and an
    inner error with more descriptive details.

    :ivar code: Enums containing high level error codes. Possible values include:
     "InvalidRequest", "InvalidArgument", "InternalServerError", "ServiceUnavailable",
     "ResourceNotFound", "Unauthorized", "RequestRateTooHigh".
    :vartype code: str
    :ivar message: Gets high level error message.
    :vartype message: str
    :ivar target: Gets the source of the error.
     For example it would be "documents" or "document id" in case of invalid document.
    :vartype target: str
    """

    def __init__(
        self,
        **kwargs
    ):
        # type: (**Any) -> None
        self.code = kwargs.get('code', None)
        self.message = None
        self.target = None

    @classmethod
    def _from_generated(cls, error):
        return cls(
            code=error.code,
            message=error.message,
            target=error.target
        )


class FileFormat(object):
    """FileFormat.

    :ivar format: Name of the format.
    :vartype format: str
    :ivar file_extensions: Supported file extension for this format.
    :vartype file_extensions: list[str]
    :ivar content_types: Supported Content-Types for this format.
    :vartype content_types: list[str]
    :ivar versions: Supported Version.
    :vartype versions: list[str]
    """

    def __init__(
        self,
        **kwargs
    ):
        # type: (**Any) -> None
        self.format = kwargs.get('format', None)
        self.file_extensions = kwargs.get('file_extensions', None)
        self.content_types = kwargs.get('content_types', None)
        self.versions = kwargs.get('versions', None)

    @classmethod
    def _from_generated(cls, file_format):
        return cls(
            format=file_format.format,
            file_extentions=file_format.file_extentions,
            content_types=file_format.content_types,
            versions=file_format.versions
        )

    @classmethod
    def _from_generated_list(cls, file_formats):
        return list( [ FileFormat._from_generated(file_formats) for file_formats in file_formats ] ) 
