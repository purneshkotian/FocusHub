import React from "react";
import { Card, CardContent, Typography, Button } from "@mui/material";

const TaskCard = ({ task, onDetail }) => {
  return (
    <Card className="m-4 border border-gray-200 shadow-md hover:shadow-lg">
      <CardContent>
        <Typography variant="h5">{task.title}</Typography>
        <Typography variant="body2" color="text.secondary">
          {task.description}
        </Typography>
        <Button
          onClick={() => onDetail(task.id)}
          className="mt-2"
          variant="contained"
          color="primary"
        >
          View Details
        </Button>
      </CardContent>
    </Card>
  );
};

export default TaskCard;
