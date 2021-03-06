# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_recognize_receipts_from_url_async.py

DESCRIPTION:
    This sample demonstrates how to recognize US sales receipts from a URL.

USAGE:
    python sample_recognize_receipts_from_url_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer API key
"""

import os
import asyncio


class RecognizeReceiptsFromURLSampleAsync(object):

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]

    async def recognize_receipts_from_url(self):
        # [START recognize_receipts_from_url_async]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer.aio import FormRecognizerClient
        async with FormRecognizerClient(
            endpoint=self.endpoint, credential=AzureKeyCredential(self.key)
        ) as form_recognizer_client:
            url = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"
            receipts = await form_recognizer_client.recognize_receipts_from_url(receipt_url=url)

            for idx, receipt in enumerate(receipts):
                print("--------Recognizing receipt #{}--------".format(idx))
                print("Receipt Type: {} has confidence: {}".format(receipt.receipt_type.type, receipt.receipt_type.confidence))
                print("Merchant Name: {} has confidence: {}".format(receipt.merchant_name.value, receipt.merchant_name.confidence))
                print("Transaction Date: {} has confidence: {}".format(receipt.transaction_date.value, receipt.transaction_date.confidence))
                print("Receipt items:")
                for item in receipt.receipt_items:
                    print("...Item Name: {} has confidence: {}".format(item.name.value, item.name.confidence))
                    print("...Item Quantity: {} has confidence: {}".format(item.quantity.value, item.quantity.confidence))
                    print("...Individual Item Price: {} has confidence: {}".format(item.price.value, item.price.confidence))
                    print("...Total Item Price: {} has confidence: {}".format(item.total_price.value, item.total_price.confidence))
                print("Subtotal: {} has confidence: {}".format(receipt.subtotal.value, receipt.subtotal.confidence))
                print("Tax: {} has confidence: {}".format(receipt.tax.value, receipt.tax.confidence))
                print("Tip: {} has confidence: {}".format(receipt.tip.value, receipt.tip.confidence))
                print("Total: {} has confidence: {}".format(receipt.total.value, receipt.total.confidence))
                print("--------------------------------------")
        # [END recognize_receipts_from_url_async]


async def main():
    sample = RecognizeReceiptsFromURLSampleAsync()
    await sample.recognize_receipts_from_url()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
