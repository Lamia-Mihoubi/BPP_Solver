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
// the variable "lists" should be filled with results that we'll get from backend 
// once the validation btn is clicked we send a request and we save the answer on lists
// in this version im using a json data file to get results from it 
const lists2 = [
    {
      key: "BB",
      label: "Branch and Bound",
      nb: "2",
      texec:"0.01",
      boites: [
        {
          idbin: "01",
          objects:[
              {
                poid:"5"
              },
              {
                poid:"6"
              },
              {
                poid:"5"
              },
              {
                poid:"3"
              },
              {
                poid:"5"
              }
          ]
        },
        {
            idbin: "02",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          }
      ]
    },
    {
        key: "DP",
        label: "Programmation dynamique",
        nb: "7",
        texec:"0.01",
        boites: [
          {
            idbin: "1",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          }
        ]
      },
      {
        key: "AG",
        label: "Algorithme genetique",
        nb: "2",
        texec:"0.01",
        boites: [
          {
            idbin: "01",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          },
          {
            idbin: "02",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          },
          {
            idbin: "03",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          },
          {
            idbin: "04",
            objects:[
                {
                  poid:"5"
                },
                {
                  poid:"6"
                },
                {
                  poid:"5"
                },
                {
                  poid:"3"
                },
                {
                  poid:"5"
                }
            ]
          },
    
         ]
        }]


class MainContent1 extends React.Component{
    constructor(props) {
        super(props)
        this.state={
            display_choosemthd: 1 ,
            display_showresults:0 
        }
        this.handleValider= this.handleValider.bind(this)
        this.handleretour= this.handleretour.bind(this)
    }

    handleValider(){

        this.setState({
            display_choosemthd:0,
            display_showresults:1
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
            content= <ChooseMthd handleValider={this.handleValider}></ChooseMthd>
       }
       if(this.state.display_showresults){
            content= <ShowResults n='5' c='10' sol_opt ='1' solutions={lists} handleretour={this.handleretour} ></ShowResults>
       } 
        return(
            <Container className={classes.root}>     
            <Typography variant="h3" className={classes.pagetitle} gutterBottom>
                Construire Votre propre Instance 
            </Typography>  
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
        minWidth: 120,
    },
    empty:{
        height:'9vw',
    }

    
      
})  
export default withStyles(styles)(MainContent1);

