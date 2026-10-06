from langchain_typesafe import Noul, TypeSafeClassifier
from dotenv import load_dotenv

load_dotenv()  # Load TYPESAFE_API_KEY from the .env file

classifier = TypeSafeClassifier()

response = classifier.invoke({
    "state": (
        "The deploy failed twice and customers are seeing 500s. "
        "Can someone look now?"
    ),
    "questions": {
        "urgent": Noul(
            instructions="Does this need attention right now?"
        ),
    },
})

urgency = response.nouls["urgent"].noul
print(urgency)