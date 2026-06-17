complaint = input("Enter customer complaint: ").lower()

if "delivery" in complaint or "late" in complaint:
    print("Issue Type: Delivery Problem")
elif "payment" in complaint or "refund" in complaint:
    print("Issue Type: Payment Issue")
elif "product" in complaint or "damaged" in complaint:
    print("Issue Type: Product Issue")
elif "service" in complaint or "support" in complaint:
    print("Issue Type: Service Issue")
else:
    print("Issue Type: General Complaint")
