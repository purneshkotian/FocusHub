import React, { useState } from "react";
import { TextField, Button, Typography } from "@mui/material";
import axios from "../services/api";
import Navbar from "../components/NavBar";

const CreateTask = () => {
  const [task, setTask] = useState({
    title: "",
    description: "",
    assigned_to: "1",
    status: "Pending",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setTask({ ...task, [name]: value });
    console.log(task);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("/tasks/", task).then((response) => {
      console.log("Task Created", response.data);
    });
  };

  return (
    <div>
      <Navbar />
      <div className="container mx-auto p-4">
        <Typography variant="h4" className="mb-4">
          Create New Task
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Title"
            name="title"
            value={task.title}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Description"
            name="description"
            value={task.description}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
            className="mt-4"
          >
            Create Task
          </Button>
        </form>
      </div>
    </div>
  );
};

export default CreateTask;
