import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container'
import { makeStyles } from '@material-ui/core/styles'
import { MDBContainer, MDBInputGroup, MDBBtn } from "mdbreact";
import ChooseMthd from './ChooseMthd';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import { withStyles } from '@material-ui/core/styles';
import ShowResults from './ShowResults'
import listefiles from '../data/instances_scholl'
const files = [{
    class: 1,
    name_file:'N1C1W1_D.txt',
  },{
    class: 1,
    name_file:'N1C1W2_D.txt',
  },{
    class: 1,
    name_file:'N1C1W1_F.txt',
  },{
    class: 1,
    name_file:'N1C1W2_5.txt',
  }]
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

class SchollPage extends React.Component{
    state1 = {
      value: 0
    }
    
    constructor(props) {
        super(props)
        this.state={
            display_choosemthd: 1 ,
            display_showresults:0 
        }
        this.handleValider= this.handleValider.bind(this)
        this.handleretour= this.handleretour.bind(this)

        this.handleChange = this.handleChange.bind(this);
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
    getinstance=()=>{
      var val = document.getElementById('select-ops').value;
      let file={
        classe:val.split(' ')[1],
        name_file:val.split(' ')[3]
      }
      
      console.log(JSON.stringify(file))
    }
    initS=()=>{
      if(this.state1.value<1){
        let selectBox=document.getElementById('select-ops')
        for(let i=0;i<listefiles.length;i++){
          for(let j=0;j<listefiles[i].length;j++){
            // create option using DOM
            const newOption = document.createElement('option');
            const optionText = document.createTextNode("Classe "+listefiles[i][j].classe+" : "+listefiles[i][j].name_file.split('.')[0]);
            // set option text
            newOption.appendChild(optionText);
            // add the option to the select box
            selectBox.appendChild(newOption);
          }

        }
        this.state1.value=this.state1.value+1
      }
      
        
    }
    handleChange(selectorFiles)
    {
        let ch=document.querySelector('#label-file')
        ch.textContent=selectorFiles[0].name
        console.log(selectorFiles[0].name);
    }
    render(){
        const classes=this.props;
        let content ;
        if(this.state.display_choosemthd){
            content= <ChooseMthd handleValider={this.handleValider}></ChooseMthd>
       }
       if(this.state.display_showresults){
            content= <ShowResults n='5' c='10' sol_opt ='1' solutions={lists2} handleretour={this.handleretour} ></ShowResults>
       }
        return(

            <Container className="container-style2">
            <Card className="card-style2"/*className={classes.typo}*/>
                <CardContent>
                    <h1>Utiliser les Instances du Benchmark Scholl </h1> 
                    <div className="input-group">
                    <div className="custom-file">
                        <input
                        type="file"
                        className="custom-file-input"
                        id="inputGroupFile01"
                        color="teal lighten-2"
                        aria-describedby="inputGroupFileAddon01"
                        onChange={ (e) => this.handleChange(e.target.files) } />
                        />
                        <label className="custom-file-label" id="label-file" htmlFor="inputGroupFile01"color="teal lighten-2">
                        Choisissez un fichier
                        </label>
                    </div>
                    </div>
                    <div >
                        <select onChange={this.getinstance} button onClick={this.initS} className="browser-default custom-select" id="select-ops">
                            <option>Choisissez une instance</option>
                        </select>
                    </div>
                </CardContent> 
            </Card>
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


export default withStyles(styles)(SchollPage);