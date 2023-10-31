from .default import api_v2, BASE
from typing import Union, List
import requests

class Search(BASE):
    def __init__(self, host: str=api_v2, api_key: str=None):
        super().__init__(host=host, api_key=api_key)
    
    def _check_string_or_list(self, hash_data):
        if isinstance(hash_data, str):
            return api_v2 + "search/hash", {"hash": hash_data}
        elif isinstance(hash_data, list):
            return api_v2 + "search/hashes", { f"hashes[{i}]": hash for i, hash in enumerate(hash_data)}
        else:
            raise TypeError("hash must be str or list")
    
    def by_hash(self, hash_data: Union[str, List]=None):
        """_summary_

        Parameters
        ----------
        hash_data : Union[str, List], optional
            _description_, by default None

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        ValueError
            _description_
        """
        url, data = self._check_string_or_list(hash_data)
        status, r = self._post(url=url, data=data, headers=self._header)
        if status == 200:
            return r.json()
        else:
            print(r.json())
            raise ValueError(f"Status code is {status}.")

