import React from "react";
import ReactDOM from "react-dom";
import "./styles.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SiteLayout from "./SiteLayout";

import "antd/dist/antd.css";
import Data from "./pages/Data";
import Visualization from "./pages/Visualization";
import Home from "./pages/Home";

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
