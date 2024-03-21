import { Box, Stack, Typography } from "@mui/material";
import { theme } from "../components/Layout";

const bannerStyle = {
    height:300,
    width:"100%",
    justifyContent:"center",
    backgroundColor:theme.light.palette.secondary.dark, 
    color:"white"
}

export default function Home() {
    return (<>
        <Stack sx={bannerStyle}>

            <Typography variant="h3" align="center">
                <strong style={{fontWeight:"bolder"}}>LinkUp:</strong> Where Service Meets Success!
            </Typography>

        </Stack>
    </>)
}