class Topic:
    def __init__(self, topicID: str, title: str, desc: str) -> None:
        self.topicID: str = topicID
        self.title: str = title
        self.desc: str = desc
        self.questions: list[Question] = list()


class Question:
    pass