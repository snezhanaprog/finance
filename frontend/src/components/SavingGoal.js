import React, { useState, useEffect } from "react";
import axios from "axios";

function SavingsGoal() {
  const [goals, setGoals] = useState([]);
  const [newGoal, setNewGoal] = useState("");

  useEffect(() => {
    axios.get("http://localhost:8000/saving_goals/")
      .then(response => {
        setGoals(response.data);
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
      });
  }, []);

  const handleGoalChange = event => {
    setNewGoal(event.target.value);
  };

  const handleFormSubmit = event => {
    event.preventDefault();

    axios.post("http://localhost:8000/saving_goals/", { title: newGoal })
      .then(response => {
        setGoals([...goals, response.data]);
        setNewGoal("");
      })
      .catch(error => {
        console.error('Ошибка при отправке данных:', error);
      });
  };

  return (
    <div>
      <h1>Цели сбережения</h1>
      {goals.map(goal => (
        <div key={goal.id}>
          <h2>{goal.title}</h2>
        </div>
      ))}
      <form onSubmit={handleFormSubmit}>
        <input type="text" value={newGoal} onChange={handleGoalChange} placeholder="Новая цель" />
        <button type="submit">Создать цель</button>
      </form>
    </div>
  );
}

export default SavingsGoal;