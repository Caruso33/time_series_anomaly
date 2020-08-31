import React from "react";
import { Layout, Menu, Typography } from "antd";
import { withRouter } from "react-router-dom";

function SiteLayout({ children, location, history }) {
  const { pathname } = location;

  const navigateTo = (path) => history.push(path);

  return (
    <Layout style={{ height: "100vh" }}>
      <Layout.Header style={{ position: "fixed", zIndex: 1, width: "100%" }}>
        <Menu
          theme="dark"
          mode="horizontal"
          selectedKeys={[pathname.slice(1) || "home"]}
        >
          <Menu.Item key="home" onClick={() => navigateTo("/")}>
            Home
          </Menu.Item>

          <Menu.Item key="data" onClick={() => navigateTo("/data")}>
            Data
          </Menu.Item>

          <Menu.Item
            key="visualization"
            onClick={() => navigateTo("/visualization")}
          >
            Visualization
          </Menu.Item>
        </Menu>
      </Layout.Header>

      <Layout.Content style={{ padding: "50px 50px", marginTop: 64 }}>
        {children}
      </Layout.Content>

      <Layout.Footer style={{ textAlign: "center" }}>
        <Typography.Text>Zykluszeiten</Typography.Text>
      </Layout.Footer>
    </Layout>
  );
}

export default withRouter(SiteLayout);
