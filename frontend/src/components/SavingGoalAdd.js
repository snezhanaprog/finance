import React, { useState, useEffect } from 'react';
import axios from 'axios';

function SavingGoalAdd() {
  const [newGoal, setNewGoal] = useState('');

  useEffect(() => {}, []);

  const handleGoalChange = event => {
    setNewGoal(event.target.value);
  };

  const handleFormSubmit = event => {
    event.preventDefault();

    axios
      .post('http://localhost:8000/saving_goals/', { title: newGoal })
      .then(response => {
        setNewGoal('');
      })
      .catch(error => console.error('Ошибка при отправке данных:', error));
  };

  return (
    <>
      <h1>Добавить цель</h1>
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          value={newGoal}
          onChange={handleGoalChange}
          placeholder="Новая цель"
        />
        <button type="submit">Создать цель</button>
      </form>
    </>
  );
}

export default SavingGoalAdd;
