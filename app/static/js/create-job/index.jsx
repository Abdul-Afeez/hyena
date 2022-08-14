const web_masters = JSON.parse(document.getElementById('create-job').textContent);
const CreateJob = ({web_masters})=>{
    React.useEffect(() => {
    }, []);
    const [state, setState] = React.useState({
        status : '',
        url: '',
        web_master_id: ''
    });

    const handleChange = ({target: { name, value}}) => {
        const new_state = {...state};
        new_state[name] = value;
        setState({...new_state});
    };

    const onSubmit = (e) => {

    };
    return (
        <form method="POST">
            <div className="col-md-4 col-sm-6">
                <div className="mt-2">
                    <label>Status</label>
                    <br/>
                    <select className="form-control" name="status" value={state.status} onChange={handleChange} id="status">
                        <option value="QUEUED">QUEUED</option>
                        <option value="PENDING">PENDING</option>
                        <option value="RUNNING">RUNNING</option>
                        <option value="RAN">RAN</option>
                        <option value="TIMEOUT">TIMEOUT</option>
                        <option value="FAILED">FAILED</option>
                    </select>
                </div>
                <div className="mt-2">
                    <label>Url</label>
                    <br/>
                    <input className="form-control" type="text" name="url" value={state.url} size={8} onChange={handleChange}/>
                </div>
                <div className="mt-2">
                    <label>WebMaster</label>
                    <br/>
                    <select className="form-control" name="web_master_id" value={state.web_master_id} onChange={handleChange} id="web_master_id">
                        <option value=""/>
                        {
                            web_masters.map((web_master) => <option  key={web_master.id} value={web_master.id}>{web_master.name}</option>)
                        }
                    </select>
                </div>
                <br/>
                <div className="align-self-end">
                    <button onClick={onSubmit} className="btn btn-primary">Create</button>
                </div>
            </div>
            <br/>
        </form>
    )
};

ReactDOM.render(<CreateJob web_masters={web_masters} />, document.getElementById('create-job'));
