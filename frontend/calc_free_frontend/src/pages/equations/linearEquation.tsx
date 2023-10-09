import React, { useEffect } from "react";
import { useState } from "react";
import {
  Grid,
  TextField,
  TextareaAutosize,
  Button,
  Typography,
  IconButton,
} from "@mui/material";
import InfoIcon from "@mui/icons-material/Info";
import LinearEquationService from "../../services/equations/linearEquationService";
import { emptyGraph } from "../../assets/graphImage";
import Validator from "../../validators/validator";
import { OverlayTrigger, Popover } from "react-bootstrap";
import "../../css/popover.css";

export interface Equation {
  equation: string;
}

export interface EquationResult {
  solution: string;
  hint: string;
  graph: string;
}

export interface EquationError {
  equation: string;
}

const LinearEquation = () => {
  const [eq, setEq] = useState<Equation>({
    equation: "",
  });
  const [res, setRes] = useState<EquationResult>({
    solution: "",
    hint: "",
    graph: emptyGraph,
  });

  const [errors, setErrors] = useState<EquationError>({
    equation: "",
  });

  const [hint, setHint] = useState<boolean>(false);

  const showOrHideHint = () => {
    setHint(!hint);
  };

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const [pop, setPop] = useState<boolean>(false);

  const setPopover = (val: boolean) => {
    setPop(val);
  };

  const solveLinearEquation = () => {
    let newErrorState = { ...errors };
    newErrorState.equation = "";
    let valid = true;
    if (!Validator.checkIfIsNotEmpty(eq.equation)) {
      newErrorState.equation = Validator.emptyMessage;
      valid = false;
    } else if (!Validator.checkMinimumLength(eq.equation, 1)) {
      newErrorState.equation = Validator.notMinLengthMessage;
      valid = false;
    } else if (!Validator.checkNotContainsZeroOnStart(eq.equation)) {
      newErrorState.equation = Validator.linearEquationStartsFromZeroMessage;
      valid = false;
    } else if (!Validator.checkIfIsValidLinearEquation(eq.equation)) {
      newErrorState.equation = Validator.invalidEquationMessage;
      valid = false;
    }
    setErrors(newErrorState);
    if (valid === true) {
      LinearEquationService.solveLinearEquation(eq)
        .then((response) => {
          setRes(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  };

  const popover = (
    <Grid marginLeft={2}>
      {pop && (
        <Popover
          id="popover-basic"
          onClick={() => {
            setPopover(false);
          }}
          onMouseLeave={() => {
            setPopover(false);
          }}
        >
          <Popover.Header id="popoverHeader" as="h3" color="#cccccc">
            Jak wpisywać równanie?
          </Popover.Header>
          <Popover.Body id="popoverBody">
            Należy wpisać lewą strone równania. <br />
            Równanie powinno być postaci ax+b. <br />
            Podawanie parametru a oraz b nie jest <br />
            konieczne. Przykładowe poprawne równania: <br />
            5x+6
            <br />
            x+4
            <br />
            -6x
            <br />
            -2,25x+7
          </Popover.Body>
        </Popover>
      )}
    </Grid>
  );

  return (
    <Grid
      container
      justifyContent="center"
      display="flex"
      alignItems="center"
      marginTop={2}
    >
      <Grid item width={1000}>
        <Grid item>
          <Grid
            item
            justifyContent="center"
            alignItems="center"
            paddingBottom={2}
            marginTop={0}
            paddingTop={0}
          >
            <Typography fontSize={40} color="#3596FC" textAlign="center">
              Równanie liniowe
            </Typography>
          </Grid>
          <Grid item width={1000} display="flex">
            <TextField
              id="equation"
              fullWidth
              placeholder="Wpisz równanie liniowe..."
              value={eq.equation ? eq.equation : ""}
              onChange={(event) =>
                setEq({ ...eq, equation: event.target.value })
              }
              helperText={errors.equation ? errors.equation : ""}
            ></TextField>
            <Typography fontSize={36}>&nbsp;=&nbsp;0&nbsp;</Typography>
            <OverlayTrigger
              trigger="click"
              rootClose
              placement="left"
              overlay={popover}
            >
              <IconButton
                id="popoverButton"
                onClick={() => {
                  setPopover(true);
                }}
              >
                <InfoIcon />
              </IconButton>
            </OverlayTrigger>
          </Grid>
          <Grid item marginTop={2}>
            <Button
              id="solve"
              fullWidth
              variant="contained"
              style={{ background: "#4683E6" }}
              onClick={() => {
                solveLinearEquation();
              }}
            >
              Rozwiąż
            </Button>
          </Grid>
        </Grid>
        <Grid item marginTop={3}>
          <Grid item>
            <Typography fontSize={16} color="#2C74B3" textAlign="left">
              Wynik
            </Typography>
          </Grid>
          <TextareaAutosize
            id="result"
            minRows={2}
            readOnly={true}
            value={res.solution ? res.solution : ""}
            style={{ width: 1000, resize: "vertical", background: "#D8E8EE" }}
          />
        </Grid>
        <Grid item marginTop={3} width={1000}>
          <Button
            id="hintButton"
            style={{
              backgroundColor: "#21b6ae",
            }}
            fullWidth
            variant="contained"
            onClick={() => {
              showOrHideHint();
            }}
          >
            {hint ? "Ukryj wskazówkę" : "Pokaż wskazówkę"}
          </Button>
        </Grid>
        <Grid item marginTop={2}>
          {hint && (
            <Grid item>
              <Grid item>
                <Typography fontSize={16} color="#2C74B3" textAlign="left">
                  Wskazówka
                </Typography>
              </Grid>
              <TextareaAutosize
                id="hint"
                readOnly={true}
                minRows={2}
                value={res.hint ? res.hint : ""}
                style={{
                  width: 1000,
                  resize: "vertical",
                  background: "#dcedc8",
                }}
              />
            </Grid>
          )}
        </Grid>
        <Grid item marginTop={2} width={1000} marginLeft={21}>
          <img
            id="image"
            src={`data:image/jpeg;base64,${res.graph}`}
            alt="Wykres funkcji"
          />
        </Grid>
      </Grid>
    </Grid>
  );
};

export default LinearEquation;
