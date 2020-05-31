import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container'
import { makeStyles } from '@material-ui/core/styles'


class SchollPage extends React.Component{
    
    render(){
        return(
            <Container >
                <Typography /*className={classes.typo}*/>
                   <h1>Here we let user pick from a list of scholl instances</h1> 
                </Typography>
            </Container>
            
            );
    }
}



export default SchollPage;