import Layout from "../components/Layout";
import Home from "../pages/Home";

const mainRoutes = {
    path:"",
    element: <Layout />,
    children:[
        {
            path:"/",
            element: <Home />
        }
    ]
}

export default mainRoutes;