import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container'
import FormNC from './FormNC'
import ChooseMthd from './ChooseMthd';

class MainContent1 extends React.Component{

    render(){
        return(
            <Container >
                <h1>Générer une instance aléatoire</h1>
                <FormNC props />
                <ChooseMthd handleValider={this.handleValider}></ChooseMthd>
            </Container>
            
            );
    }
}


export default MainContent1;