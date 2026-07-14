from lime.lime_text import LimeTextExplainer


explainer = LimeTextExplainer(

    class_names=[
        "Real Job",
        "Fake Job"
    ]

)


def generate_lime_explanation(text, model, vectorizer):

    def predict_probability(texts):

        vectors = vectorizer.transform(texts)

        return model.predict_proba(vectors)

    explanation = explainer.explain_instance(

        text,

        predict_probability,

        num_features=5

    )

    return explanation.as_list()