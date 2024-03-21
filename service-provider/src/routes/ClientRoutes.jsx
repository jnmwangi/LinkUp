import { useRoutes } from "react-router-dom";
import mainRoutes from "./main-routes";

export default function ClientRoutes(){
    return useRoutes([mainRoutes])
}