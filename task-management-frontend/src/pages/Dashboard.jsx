import React, { useEffect, useState } from "react";
import axios from "../services/api";
import TaskCard from "../components/TaskCard";
import Navbar from "../components/NavBar";

const Dashboard = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get("/tasks/").then((response) => setTasks(response.data));
  }, []);

  const handleTaskDetail = (taskId) => {
    console.log(`Navigating to details of task ID: ${taskId}`);
  };

  return (
    <div>
      <Navbar />
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold">Task Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {tasks.map((task) => (
            <TaskCard key={task.id} task={task} onDetail={handleTaskDetail} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
