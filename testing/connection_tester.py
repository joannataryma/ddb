from agent.agent import Agent

if __name__ == "__main__":

    mqtt_agent = Agent()

    try:
        mqtt_agent.publish("makowiec")
    except Exception as e:
        print e