from django.contrib import admin

from .models import DetachedSignature, EmbeddedSignature


@admin.register(DetachedSignature)
class DetachedSignatureAdmin(admin.ModelAdmin):
    list_display = (
        'document_file', 'date_time', 'key_id', 'signature_id',
        'public_key_fingerprint', 'signature_file'
    )
    list_display_links = ('document_file',)


@admin.register(EmbeddedSignature)
class EmbeddedSignatureAdmin(admin.ModelAdmin):
    list_display = (
        'document_file', 'date_time', 'key_id', 'signature_id',
        'public_key_fingerprint'
    )
    list_display_links = ('document_file',)
