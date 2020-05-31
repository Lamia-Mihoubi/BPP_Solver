import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container'


class MainContent1 extends React.Component{
    
    render(){
        return(
            <Container >
                <Typography /*className={classes.typo}*/>
                   <h1>Here we geenrate aleatoirement des instances and show les resultats</h1> 
                </Typography>
            </Container>
            
            );
    }
}


export default MainContent1;