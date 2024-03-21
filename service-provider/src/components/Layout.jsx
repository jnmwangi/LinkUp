import { Outlet } from "react-router-dom";
import { createTheme } from '@mui/material/styles'
import { blueGrey, brown, purple } from "@mui/material/colors";
import { ThemeProvider } from "@emotion/react";

export const theme = {
    light: createTheme({
        palette: {
            primary: {
                main: blueGrey[500]
            },
            secondary: {
                main: brown[500]
            }
        }
    }),
    dark: createTheme({
        palette: {
            primary: {
                main: blueGrey[500]
            },
            secondary: {
                main: brown[500]
            }
        }
    })
}

export default function Layout() {
    return (<>
        <ThemeProvider theme={theme['light']}>
            <Outlet />
        </ThemeProvider>
    </>);
}