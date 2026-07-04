from backend.workflow import initialize_workflow

# Change this to one of your sample PDFs
file_path = "sample_documents\\High_Risk_Sale_Deed_AI_Testing.pdf"

result = initialize_workflow(file_path)

print("\n========== WORKFLOW RESULT ==========\n")

print("Status:", result["status"])
print("Error:", result["error"])
print("Metadata:", result["metadata"])
print("Chunks:", len(result["chunks"]))

print("\nWorkflow completed successfully!")