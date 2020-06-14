import { Component } from "react";
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


class PickFile extends Component{
    constructor(props) {
        super(props)
        this.state = {
        value: 0,
        classe:0,
        filename: "",
      }
    }
    
    getinstance=()=>{
        var val = document.getElementById('select-ops').value;
        let file={
          classe:val.split(' ')[1],
          name_file:val.split(' ')[3]
        }
        this.setState({
          classe:val.split(' ')[1],
          filename: val.split(' ')[3]
        })
        console.log(JSON.stringify(file))
        this.props.sendfilename(val.split(' ')[1], val.split(' ')[3])
      }
      initS=()=>{
        if(this.state.value<1){
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
          this.state.value=this.state.value+1
        }
        
          
      }
      handleChange(selectorFiles)
      {
          let ch=document.querySelector('#label-file')
          ch.textContent=selectorFiles[0].name
          let file={
            name_file:selectorFiles[0].name
          }
          console.log(JSON.stringify(file));
      }

    render(){
        const {classes}=this.props;

        return (
            <div>
            <Card className={classes.root}>
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
            </div>
        );
    }
}

const styles = theme => ({
    root: {
        //backgroundColor: '#020F59',
        margin: theme.spacing(3),
        width: "69vw",
       
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

export default withStyles(styles)(PickFile);