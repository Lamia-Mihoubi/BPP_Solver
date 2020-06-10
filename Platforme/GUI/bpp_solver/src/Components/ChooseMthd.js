import React from 'react';
import Container from '@material-ui/core/Container'
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import { withStyles } from '@material-ui/core/styles';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import FormLabel from '@material-ui/core/FormLabel';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import Instance from './Instance'
import PickFile from './PickFile'
import FormNC from './FormNC'

class ChooseMthd extends React.Component{
    constructor(props) {
        super(props)
        this.state={
            n : 0,
            c: 0 , 
            list : [],
            classe : 0 ,
            filename: "",
            checked_BB:0,
            checked_DP: 0, 
            checked_BF:0,
            checked_BFD :0,
            checked_FF:0,
            checked_FFD:0 , 
            checked_NF:0,
            checked_NFD:0 ,
            checked_AG:0,
            checked_WOA:0,
            checked_ILWOA:0,
            checked_RS: 0, 
            RS_nb_iter:1000,
            RS_alpha:0.925,
            WOA_a:10,
            WOA_b:8.96, 
            WOA_max_iter:117,
            WOA_nb_whales:30,
            ILWOA_nb_agents:10,
            ILWOA_beta:1.5,
            ILWOA_a:20,
            ILWOA_b:7.36, 
            ILWOA_max_iter:30,
            AG_popSize:10,
            AG_K:20,
            AG_nb_gen:200
        }
        this.ValiderClick=this.ValiderClick.bind(this)
        this.reinitClick = this.reinitClick.bind(this)
        this.set_n_c_list = this.set_n_c_list.bind(this)
        this.set_class_file= this.set_class_file.bind(this)
    }
    set_n_c_list(n,c,list){
        this.setState({
            n:n,
            c:c,
            list: list, 
        });
    }
    set_class_file(classe, filename){
        this.setState({
            classe:classe, 
            filename: filename,
        })
    }
    async ValiderClick(){
        const page = this.props.pagenum // pour savoir quelle page we're in et donc quelle requete envoyer
        // get selected data
        const state_JSON = JSON.stringify(this.state);
                //send request 
        if(page==1 | page==2){
        const response= await fetch('/resultats',{
            headers: {
                'Content-Type': 'application/json'
              }, 
              method: 'POST',
              body: state_JSON
        })
        const jsonres = await response.json();
            // get the result and sent the json answer direct 
            //window.alert(jsonres['n']); //for test
            this.props.handleValider(jsonres);
        }

        if(page==3){
            const response= await fetch('/benchmark',{
                headers: {
                    'Content-Type': 'application/json'
                  }, 
                  method: 'POST',
                  body: state_JSON
            })
            const jsonres = await response.json();
                // get the result and sent the json answer direct 
               // window.alert(jsonres['Fname']);
                this.props.handleValider(jsonres);
        }
            //this.props.handleValider("");
    
    };
    reinitClick(){
        //recopy the same initialisaiton of the constructor here 
        this.setState({
            checked_BB:0,
            checked_DP: 0, 
            checked_BF:0,
            checked_BFD :0,
            checked_FF:0,
            checked_FFD:0 , 
            checked_NF:0,
            checked_NFD:0 ,
            checked_AG:0,
            checked_WOA:0,
            checked_ILWOA:0,
            checked_RS: 0, 
            RS_nb_iter:1000,
            RS_alpha:0.925,
            WOA_a:10,
            WOA_b:8.96, 
            WOA_max_iter:117,
            WOA_nb_whales:30,
            ILWOA_nb_agents:10,
            ILWOA_beta:1.5,
            ILWOA_a:20,
            ILWOA_b:7.36, 
            ILWOA_max_iter:30,
            AG_popSize:10,
            AG_K:20,
            AG_nb_gen:200        
        });        
    }
    render(){
        const { classes } = this.props;        
        const handleChange = (event) => {
            this.setState({ ...this.state, [event.target.name]: event.target.checked });
          };
          const handleChangeparams = (event) => {
            const name = event.target.name;
            this.setState({
              ...this.state,
              [name]: event.target.value,
            });
          };
        const methodss = 
        <Container className={classes.root}>
        
        <Card /*className={classes.root}*/>
            <CardHeader textsize='13'
                title={"Choisir la méthode de résolution"}
            />

            <CardContent>
                <FormLabel component="legend">Méthodes Exactes</FormLabel>
                <FormGroup row >
                    <FormControlLabel
                        control={
                                <Checkbox 
                                    checked={this.state.checked_BB} 
                                    onChange={handleChange} 
                                    name="checked_BB" 
                                    />}
                        label="Branch and Bound"
                        />
                    <FormControlLabel
                        control={
                                <Checkbox
                                    checked={this.state.checked_DP}
                                    onChange={handleChange}
                                    name="checked_DP"
                                 />
                                }
                        label="Programmation dynamique"
                        />     
                </FormGroup>
                <FormLabel className={classes.formLabel} component="legend">Heuristiques</FormLabel>
                    <FormGroup row >
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_FF} 
                                        onChange={handleChange} 
                                        name="checked_FF" 
                                        />}
                            label="First Fit"
                            />
                       
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_NF} 
                                        onChange={handleChange} 
                                        name="checked_NF" 
                                        />}
                            label="Next Fit"
                            />
                            
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_BF} 
                                        onChange={handleChange} 
                                        name="checked_BF" 
                                        />}
                            label="Best Fit"
                            />                                

                    </FormGroup>
                    <FormGroup row>                             
                        <FormControlLabel
                            control={
                                    <Checkbox
                                        checked={this.state.checked_FFD}
                                        onChange={handleChange}
                                        name="checked_FFD"
                                    />
                                    }
                            label="First Fit Decreasing"
                            />     
                        <FormControlLabel
                            control={
                                    <Checkbox
                                        checked={this.state.checked_NFD}
                                        onChange={handleChange}
                                        name="checked_NFD"
                                    />
                                    }
                            label="Next Fit Decreasing"
                            />     

                        
                        <FormControlLabel
                            control={
                                    <Checkbox
                                        checked={this.state.checked_BFD}
                                        onChange={handleChange}
                                        name="checked_BFD"
                                    />
                                    }
                            label="Best Fit Decreasing"
                            />     
                    </FormGroup>



                <FormLabel  className={classes.formLabel} component="legend">Meta heuristiques</FormLabel>
                <FormGroup  >
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_AG} 
                                        onChange={handleChange} 
                                        name="checked_AG" 
                                        />}
                            label="Genetic Algorithm"
                            />
                      <FormGroup row>
                      <formControl className={classes.formControl} >
                        </formControl>
                        <FormControl   className={classes.formControl}>
                                <InputLabel htmlFor="AG_nb_gen">nb gen</InputLabel>
                                <Select
                                native
                                value={this.state.AG_nb_gen}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'AG_nb_gen',
                                    id: 'AG_nb_gen',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={100}>100</option>
                                <option value={200}>200</option>
                                <option value={300}>300</option>
                                </Select>                                     

                        </FormControl>
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="AG_K">K</InputLabel>
                                <Select
                                native
                                value={this.state.AG_K}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'AG_K',
                                    id: 'AG_K',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={0.85}>0.85</option>
                                <option value={0.8}>0.8</option>
                                </Select>
                        </FormControl> 
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="AG_popSize">PopuSize</InputLabel>
                                <Select
                                native
                                value={this.state.AG_popSize}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'AG_popSize',
                                    id: 'AG_popSize',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={30}>30</option>
                                <option value={30}>40</option>
                                </Select>
                        </FormControl>        
                    </FormGroup>
                
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_WOA} 
                                        onChange={handleChange} 
                                        name="checked_WOA" 
                                        />}
                            label="Whale Optimization Algorithm (WOA)"
                            />
                        <FormGroup row>
                        <formControl className={classes.formControl} >
                        </formControl>
                        <FormControl   className={classes.formControl}>
                                <InputLabel htmlFor="WOA_b">b</InputLabel>
                                <Select
                                native
                                value={this.state.WOA_b}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'WOA_b',
                                    id: 'WOA_b',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={8.96}>8.96</option>
                                <option value={7.64}>7.64</option>
                                <option value={30}>1000</option>
                                </Select>                                     

                        </FormControl>
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="WOA_a">a</InputLabel>
                                <Select
                                native
                                value={this.state.WOA_a}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'WOA_a',
                                    id: 'WOA_a',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={30}>30</option>
                                <option value={30}>35</option>
                                </Select>
                        </FormControl>  
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="WOA_max_iter">max iter</InputLabel>
                                <Select
                                native
                                value={this.state.WOA_max_iter}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'WOA_max_iter',
                                    id: 'WOA_max_iter',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={117}>117</option>
                                <option value={271}>271</option>
                                <option value={30}>0.85</option>
                                <option value={30}>0.8</option>
                                </Select>
                        </FormControl>
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="WOA_nb_whales">nb whales</InputLabel>
                                <Select
                                native
                                value={this.state.WOA_nb_whales}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'WOA_nb_whales',
                                    id: 'WOA_nb_whales',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>0.925</option>
                                <option value={20}>0.90</option>
                                <option value={28}>28</option>
                                <option value={30}>30</option>
                                </Select>
                        </FormControl>            
                    </FormGroup>
                
                            
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_ILWOA} 
                                        onChange={handleChange} 
                                        name="checked_ILWOA" 
                                        />}
                            label="Improved Whale Optimization Algorithm (ILWOA)"
                            /> 
                        <FormGroup row>
                        <formControl className={classes.formControl} >
                        </formControl>
                        <FormControl   className={classes.formControl}>
                                <InputLabel htmlFor="ILWOA_b">b</InputLabel>
                                <Select
                                native
                                value={this.state.ILWOA_b}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'ILWOA_b',
                                    id: 'ILWOA_b',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={7.36}>7.36</option>
                                <option value={20}>500</option>
                                <option value={30}>1000</option>
                                </Select>                                     

                        </FormControl>
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="ILWOA_a">a</InputLabel>
                                <Select
                                native
                                value={this.state.ILWOA_a}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'ILWOA_a',
                                    id: 'ILWOA_a',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={30}>30</option>
                                <option value={30}>35</option>
                                </Select>
                        </FormControl>  
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="ILWOA_max_iter">max iter</InputLabel>
                                <Select
                                native
                                value={this.state.ILWOA_max_iter}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'ILWOA_max_iter',
                                    id: 'ILWOA_max_iter',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={30}>30</option>
                                <option value={30}>35</option>
                                </Select>
                        </FormControl>  
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="ILWOA_nb_agents">nb agents</InputLabel>
                                <Select
                                native
                                value={this.state.ILWOA_nb_agents}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'ILWOA_nb_agents',
                                    id: 'ILWOA_nb_agents',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={10}>10</option>
                                <option value={20}>20</option>
                                <option value={30}>30</option>
                                <option value={40}>40</option>
                                </Select>
                        </FormControl>
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="ILWOA_beta">beta</InputLabel>
                                <Select
                                native
                                value={this.state.ILWOA_beta}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'ILWOA_beta',
                                    id: 'ILWOA_beta',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={0.33}>0.33</option>
                                <option value={0.5}>0.5</option>
                                <option value={1.5}>1.5</option>
                                <option value={2}>2</option>
                                </Select>
                        </FormControl>
                        
                            
                    </FormGroup>
                   
                        <FormControlLabel
                            control={
                                    <Checkbox 
                                        checked={this.state.checked_RS} 
                                        onChange={handleChange} 
                                        name="checked_RS" 
                                        />}
                            label="Simulated annealing"
                            />                                  

                    </FormGroup>
                    <FormGroup row>
                    <formControl className={classes.formControl} >
                        </formControl>
                        <FormControl   className={classes.formControl}>
                                <InputLabel htmlFor="RS_nb_iter">nb iter</InputLabel>
                                <Select
                                native
                                value={this.state.RS_nb_iter}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'RS_nb_iter',
                                    id: 'RS_nb_iter',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={30}>30</option>
                                <option value={500}>500</option>
                                <option value={1000}>1000</option>
                                </Select>                                     
                                        
                        </FormControl>
                        
                        <FormControl className={classes.formControl} >
                                <InputLabel htmlFor="RS_alpha">alpha</InputLabel>
                                <Select
                                native
                                value={this.state.RS_alpha}
                                onChange={handleChangeparams}
                                inputProps={{
                                    name: 'RS_alpha',
                                    id: 'RS_alpha',
                                }}
                                >
                                <option aria-label="None" value="" />
                                <option value={0.925}>0.925</option>
                                <option value={0.9}>0.90</option>
                                <option value={0.85}>0.85</option>
                                <option value={0.8}>0.8</option>
                                </Select>
                        </FormControl>        
                    </FormGroup>
                <FormLabel component="legend" className={classes.formLabel}>Hybrid methods</FormLabel>

                <FormControlLabel
                            control={
                                    <Checkbox 
                                        //checked={this.state.checked_ILWOA} 
                                        //onChange={handleChange} 
                                        name="checked_ILWOA" 
                                        />}
                            label="Our Hybrid Method "
                            /> 
            </CardContent>
        
        </Card>

        <Button  className={classes.btn}  onClick={this.reinitClick} variant="contained" size ="large" color="primary">
                Réinitialiser
        </Button>
        <Button  className={classes.btn} onClick={this.ValiderClick} variant="contained" size ="large" color="secondary">
            Résoudre l'instance
        </Button>
    </Container>

       
        const page = this.props.pagenum 
        if(page==1){ 
            return (
        <div>
            <Instance sendpb={this.set_n_c_list}></Instance>
            {methodss}            
        </div>)}
            
        if(page==2){
             return (
             <div>
                 <h1>Générer une instance aléatoire</h1>
                 <FormNC props sendpb={this.set_n_c_list} />
                {methodss}
            </div>
            )
        }
        if(page==3){
            return (
            <div>
                <PickFile sendfilename={this.set_class_file}></PickFile>
               {methodss}
           </div>)
        }
    }
}


    
const styles = theme => ({
    root: {
        //backgroundColor: '#020F59',
      },
      drawerPaper: {
       
      },
    formControl:{
        margin: theme.spacing(1),
        minWidth: 100,
    },
    formLabel:{
        margin:theme.spacing(1)
    },
    btn:{
        margin: theme.spacing(5),
       
    }
      
})  
export default withStyles(styles)(ChooseMthd);

