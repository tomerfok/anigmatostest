import React from 'react';

import {
  makeStyles,
  Container,
  Typography,
  TextField,
  Button,
} from "@material-ui/core";
import { useState } from "react";

interface IFormInput {
  email: string;
  username: string;
}

const useStyles = makeStyles((theme) => ({
  heading: {
    textAlign: "center",
    margin: theme.spacing(1, 0, 4),
  },
  submitButton: {
    marginTop: theme.spacing(4),
  },
}));

function App() {
  const { heading, submitButton } = useStyles();
  const [json, setJson] = useState<string>();
  
  async function handleSubmit() {
    let myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    let respone = await fetch('http://localhost:3000/create', {
      method: 'POST', 
      mode: 'no-cors',
      headers: myHeaders,
      body: JSON.stringify(json)
    });
    return respone;
  }

  const onSubmit = (data: IFormInput) => {
    setJson(JSON.stringify(data));
  };

  return (
    <Container maxWidth="xs">
      <Typography className={heading} variant="h3">
        Sign Up Form
      </Typography>
      <form noValidate>
        <TextField
          variant="outlined"
          margin="normal"
          label="Email"
          fullWidth
          required
        />
        <TextField
          variant="outlined"
          margin="normal"
          label="Username"
          fullWidth
          required
        />
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          className={submitButton}
          onClick={handleSubmit}
        >
          Sign Up
        </Button>
        {json && (
          <>
            <Typography variant="body1">{json}</Typography>
          </>
        )}
      </form>
    </Container>
  );
}

export default App;
