import qrcode
import uuid

# Generate a unique ticket ID
ticket_id = str(uuid.uuid4())  # Example: "b8a7f5c2-3d3a-4e2b-b7a4-8d9c7d1b6b3f"

# Create QR code with only the ticket ID
qr = qrcode.make(ticket_id)
qr.save("ticket_qr.png")

print("Generated Ticket ID:", ticket_id)
