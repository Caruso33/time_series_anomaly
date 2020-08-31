import "antd/dist/antd.css";
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Data from "./pages/Data";
import Home from "./pages/Home";
import Visualization from "./pages/Visualization";
import SiteLayout from "./SiteLayout";
import "./styles.css";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <SiteLayout>
        <Switch>
          <Route path="/data">
            <Data />
          </Route>
          <Route path="/visualization">
            <Visualization />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </SiteLayout>
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);
