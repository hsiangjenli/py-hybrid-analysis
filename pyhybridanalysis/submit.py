from .default import api_v2, BASE, Environment
import os

class Submit(BASE):
    def __init__(self, host: str=api_v2, api_key: str=None, email: str=None, global_environment: Environment=Environment.ubuntu2004):
        super().__init__(host=host, api_key=api_key)
        self.email = email
        self.global_environment = global_environment
    
    def file(self, file_path: str, environment: Environment=Environment.ubuntu2004):

        """
        ::

            Submit a file to Hybrid Analysis for analysis.
        
        Parameters
        ----------
        file_path : str
            Path to the file to be submitted.
        
        environment : Environment, optional
            Environment for analysis, by Environment.ubuntu2004 
        """
        file_name = os.path.basename(file_path)
        env = environment if environment else self.global_environment
        url = api_v2 + "submit/file"
        data = {
            "environment_id": env.value, 
            "allow_community_access": True, 
            "no_share_third_party": True
        }
    
        print(f"Submitting {file_name} to Hybrid Analysis...")
        
        status, r = self._post(url=url, data=data, headers=self._header, files={'file': (file_name, open(file_path, 'rb'))})
        
        if status == 201:
            return r.json()
        else:
            print(r.text)
            raise ValueError(f"Status code is {status}.")
