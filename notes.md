# Use cases

## Order Repository

## Order Notifier

## Payment Gateway

```typescript
class ExternalPaymentGatewayAdapter implements PaymentGateway {
  private paymentService: ExternalPaymentService;

  constructor(paymentService: ExternalPaymentService) {
    this.paymentService = paymentService;
  }

  async initiatePayment(
    orderId: string,
    amount: number // doesn't seem to be needed!
  ): Promise<PaymentResult> {
    // Implement the logic to initiate payment using the external payment service
  }

  async verifyPayment(paymentId: string): Promise<PaymentStatus> {
    // Implement the logic to verify payment status using the external payment service
  }

  async refundPayment(paymentId: string): Promise<RefundResult> {
    // Implement the logic to refund payment using the external payment service
  }
}
```

### Methods:

- initiate_payment

## Shipping Gateway
