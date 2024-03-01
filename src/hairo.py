import openai

openai.api_key = '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'

def ask(question, chat_log=None):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un assistant pour étudiant de première année en médecine."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except openai.error.RateLimitError as e:
        print("Erreur de limite de taux : Vous avez dépassé votre quota actuel.")
        return "Je suis désolé, je ne peux pas répondre en ce moment."

def create_quiz(article):
    quiz = "Voici votre quiz basé sur l'article :\n\n"
    return quiz

def analyze_responses(quiz_responses):
    analysis = "Voici l'analyse de vos réponses :\n\n"
    return analysis

chat_log = []
while True:
    question = input("Vous : ")
    if question.lower() == 'stop':
        break
    elif question.lower() == 'envoyer article':
        article = input("Veuillez entrer le texte de l'article : ")
        quiz = create_quiz(article)
        print("Assistant : Quiz créé avec succès ! Veuillez répondre aux questions.")
        chat_log.append({"role": "user", "content": "J'ai envoyé un article en pièce jointe."})
    elif "quiz" in question.lower():
        if 'quiz' in locals():
            print("Assistant :", quiz)
            chat_log.append({"role": "user", "content": "Je veux faire le quiz."})
        else:
            print("Assistant : Désolé, veuillez d'abord envoyer un article en pièce jointe.")
            chat_log.append({"role": "user", "content": "Je veux faire le quiz."})
    else:
        answer = ask(question, chat_log)
        print("Assistant :", answer)
        chat_log.append({"role": "user", "content": question})
        chat_log.append({"role": "assistant", "content": answer})