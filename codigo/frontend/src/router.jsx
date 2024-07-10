export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { path: "/", element: <Home /> },
      { path: "/generatetable", element: <GenerateTable /> },
      { path: "/generatemap", element: <GenerateMap /> },
    ],
  },
]);
