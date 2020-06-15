import React from 'react';
import Container from '@material-ui/core/Container'
import { withStyles } from '@material-ui/core/styles';
import ChooseMthd from './ChooseMthd'
import ShowResults from './ShowResults'
import Typography from '@material-ui/core/Typography'
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import lists from '../data/resultats.json'
import Instance from './Instance'

// the variable "lists" should be filled with results that we'll get from backend 
// once the validation btn is clicked we send a request and we save the answer on lists
// in this version im using a json data file to get results from it 

class MainContent1 extends React.Component{
    constructor(props) {
        super(props)
        this.state={
            display_choosemthd: 1 ,
            display_showresults:0 ,
            solutions:'',
        }
        this.handleValider= this.handleValider.bind(this)
        this.handleretour= this.handleretour.bind(this)
    }

    handleValider(solution){
      // set a variable list on the state ( for dynamic UI results)
        this.setState({
            display_choosemthd:0,
            display_showresults:1,
            solutions:solution,
        });        
    }
    handleretour(){
        this.setState({
            display_choosemthd:1,
            display_showresults:0
        });
    }
    render(){
        const classes=this.props;
        let content ;
        if(this.state.display_choosemthd){
            content=<div> <ChooseMthd pagenum={1} handleValider={this.handleValider}></ChooseMthd> </div> 
       }
       if(this.state.display_showresults){
         // when backend is done change to solutions={this.state.solutions}
            content= <ShowResults n='5' c='10' sol_opt ='1' solutions={this.state.solutions} handleretour={this.handleretour} ></ShowResults>
       } 
        return(
            <Container className={classes.root}>  
             
            <div className={classes.empty}></div>    
            {content}
            
            </Container>
        )
           
    }
}
 
    
const styles = theme => ({
    root: {
        //backgroundColor: '#020F59',
      },
      drawerPaper: {
       
      },
    pagetitle:{
        margin: theme.spacing(1),
        
    },
    empty:{
        height:'9vw',
    }

    
      
})  
export default withStyles(styles)(MainContent1);

