import React from "react";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div style={{ display: "flex" }}>
      <h2>
        You have 2 main options
        <Link style={{ display: "block" }} to="/data">
          Go to see the data
        </Link>
        <Link style={{ display: "block" }} to="/visualization">
          Go to see the visualization
        </Link>
      </h2>
    </div>
  );
}
