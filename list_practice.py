study_topics = ["Python", "HTML", "CSS", "JavaScript", "FastAPI", "Docker"]
# print(study_topics)
# print(type(study_topics))

# print(study_topics[0])
# print(study_topics[4])

# study_topics.append("Docker")
# study_topics.append("Git")
# print(study_topics)
# print(len(study_topics))

# study_topics[1] = "HTML5"
# study_topics[2] = "CSS3"
# print(study_topics)
# print(len(study_topics))

# study_topics.remove("HTML")
# print(study_topics)
# study_topics.pop(1)
# print(study_topics)

study_topics.remove("CSS")
removed_element = study_topics.pop(2)
print(removed_element)
print(study_topics)