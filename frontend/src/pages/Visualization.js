import React, { useEffect, useState } from "react";
import axios from "axios";
import C3Chart from "react-c3js";
import "c3/c3.css";
import { Spin } from "antd";
import moment from "moment";

export default function Visualization() {
  const [zyklusZeit, setZyklusZeit] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    axios.get("http://127.0.0.1:8000/time_series/").then(({ data }) => {
      setIsLoading(false);

      const rows = [["timestamp", "cycle_time"]];

      for (const row of data) {
        const { timestamp, cycle_time } = row;
        const date = moment(timestamp, "DD.MM.YYYY HH:mm:ss");

        rows.push([date, cycle_time]);
      }

      setZyklusZeit(rows);
    });
  }, []);

  return isLoading ? (
    <Spin style={{ textAlign: "center", display: "block" }} />
  ) : (
    <C3Chart
      zoom={{ enabled: true, rescale: true }}
      data={{
        x: "timestamp",
        rows: zyklusZeit,
      }}
      axis={{
        x: {
          type: "timeseries",
          tick: {
            count: 8,
            format: "%d.%m.%Y %H:%M:%S",
          },
        },
      }}
     
    />
  );
}
