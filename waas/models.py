from django.db import models
from django.contrib.auth import get_user_model

from utils.choices import DOCUMENT_TYPES, PAYMENT_TYPES, TRANSACTION_TYPE_ENUM

User = get_user_model()


class DocumentType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.IntegerField(choices=DOCUMENT_TYPES, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'document_type'


class WaasAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    display_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    document_type = models.ForeignKey(
        DocumentType, default=1, on_delete=models.SET_NULL, null=True)
    document_number = models.CharField(max_length=255)
    aml_score = models.IntegerField()
    customer_account_number = models.CharField(max_length=255)
    customer_balance = models.DecimalField(max_digits=19, decimal_places=2)
    cumulative_points = models.DecimalField(max_digits=19, decimal_places=2)
    redeemed_points = models.DecimalField(max_digits=19, decimal_places=2)
    available_points = models.DecimalField(max_digits=19, decimal_places=2)
    cumulative_spent_amount = models.DecimalField(
        max_digits=19, decimal_places=2)
    status = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.display_name}-{self.customer_account_number}'

    class Meta:
        # managed = False
        db_table = 'waas_account'


class TransactionStaging(models.Model):
    transaction_reference = models.CharField(max_length=100, null=True)
    checkout_request_id = models.CharField(max_length=255, null=True)
    network_code = models.CharField(max_length=8, null=True)
    sender_account_number = models.CharField(max_length=50, null=True)
    recipient_account_number = models.CharField(max_length=50, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    points = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    transaction_fee = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00)
    waas_account = models.ForeignKey(
        WaasAccount, on_delete=models.SET_NULL, null=True)
    merchant_code = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100, null=True)
    result_description = models.CharField(max_length=255, null=True)
    transaction_type_enum = models.IntegerField()
    status = models.IntegerField(default=0)
    callback_url = models.URLField(null=True)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.waas_account.customer_account_number}-{self.amount}'

    class Meta:
        # managed = False
        db_table = 'transaction_staging'


class TransactionNotification(models.Model):
    merchant_code = models.CharField(max_length=255, null=True)
    customer_mobile = models.CharField(max_length=255, null=True)
    business_short_code = models.CharField(max_length=255, null=True)
    invoice_number = models.CharField(max_length=255, null=True)
    payment_method = models.CharField(max_length=255, null=True)
    trans_id = models.CharField(max_length=255, null=True)
    third_party_trans_id = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    transaction_type = models.CharField(max_length=255, null=True)
    msisdn = models.CharField(max_length=255, null=True)
    org_account_balance = models.CharField(max_length=255, null=True)
    trans_amount = models.CharField(max_length=255, null=True)
    trans_time = models.CharField(max_length=255, null=True)
    bill_ref_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.full_name}-{self.transaction_id}'

    class Meta:
        # managed = False
        db_table = 'transaction_notification'


class PaymentType(models.Model):
    value = models.CharField(max_length=100, null=True,
                             choices=PAYMENT_TYPES, unique=True)
    description = models.CharField(max_length=500, null=True)
    is_cash_payment = models.SmallIntegerField(default=0, null=True)
    order_position = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'payment_type'


class PaymentDetail(models.Model):
    payment_type = models.ForeignKey(
        PaymentType, null=True, on_delete=models.SET_NULL)
    account_number = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'payment_detail'


class WaasAccountTransaction(models.Model):
    account_number = models.ForeignKey(
        WaasAccount, null=True, on_delete=models.SET_NULL)
    payment_detail = models.ForeignKey(
        PaymentDetail, null=True, on_delete=models.SET_NULL)
    merchant_code = models.CharField(max_length=12)
    transaction_reference = models.CharField(max_length=255)
    transaction_type_enum = models.SmallIntegerField(
        choices=TRANSACTION_TYPE_ENUM)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    points = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    transaction_code = models.CharField(
        max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'waas_account_transaction'





