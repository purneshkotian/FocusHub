import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";

const Navbar = () => {
  return (
    <AppBar position="static" className="bg-blue-500">
      <Toolbar>
        <Typography variant="h6" className="flex-1">
          Task Management Platform
        </Typography>
        <Button color="inherit" href="/">
          Dashboard
        </Button>
        <Button color="inherit" href="/create-task">
          Create Task
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
