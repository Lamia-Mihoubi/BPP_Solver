import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container'
import { makeStyles } from '@material-ui/core/styles'


class MainContent1 extends React.Component{
    render(){
        return(
            <Container >
                <Typography >
                    <h1>Here let the user enter an instance </h1>
                </Typography>
            </Container>
            
            );
    }
}

export default MainContent1;