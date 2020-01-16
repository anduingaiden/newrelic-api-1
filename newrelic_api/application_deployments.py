from .base import Resource


class ApplicationDeployments(Resource):
    """
    An interface for interacting with the NewRelic Browser Application API.
    """

    def list(self, application_id=None, page=None):
        """
        This API endpoint returns a paginated list of the deployments associated with a given application based
        with your New Relic account.
        Browser Applications can only be filtered by the
        application IDs.
        :type application_id: int
        :param application_id: Filter by application id
        :type page: int
        :param page: Pagination index
        :rtype: dict
        :return: The JSON response of the API, with an additional 'pages' key
            if there are paginated results
        ::
            {
                "deployment": {
                    "id": "integer",
                    "revision": "string",
                    "changelog": "string",
                    "description": "string",
                    "user": "string",
                    "timestamp": "datetime",
                "links": {
                    "application": "integer"
                    }
                }
            }
        """
        filters = [
            'filter[id]={0}'.format(application_id)
            if application_id else None, 'page={0}'.format(page)
            if page else None
        ]

        return self._get(
            url='{0}deployments.json'.format(self.URL),
            headers=self.headers,
            params=self.build_param_string(filters))

    def create(self, application_id, revision, changelog, description, user):
        """
        This API endpoint creates a deployment record for a given application based with your New Relic account.
        Deployment records are created with the following attributes:
        Required:
        - Application ID
        - Revision, such as a git SHA
        Optional:
        - Changelog
        - Description
        - User posting the deployment
        - Timestamp of the deployment
        Note that the optional timestamp of the deployment must be provided in UTC and in ISO8601 format. For example,
        ‘2019-10-08T00:15:36Z’” If you have not provided a timestamp, the time of your deployment will be recorded
        as the current time in UTC.
        :type application_id: int
        :param application_id: The application_id of the application
        type revision: str
        :param revision: The application's revision such as a git SHA
        type changelog: str
        :param changelog: The changelog of the application
        type description: str
        :param description: The description of the application
        type user: str
        :param user: The user that will post the application's deployment
        :rtype: dict
        :return: The JSON response of the API
        ::
            {
                "deployment": {
                    "id": "integer",
                    "revision": "string",
                    "changelog": "string",
                    "description": "string",
                    "user": "string",
                    "timestamp": "datetime",
                    "links": {
                        "application": "integer"
                    }
                }
            }
        """

        filters = [
            'filter[id]={0}'.format(application_id) if application_id else None
        ]

        data = {{
            "deployment": {
                "revision": revision,
                "changelog": changelog,
                "description": description,
                "user": user
            }
        }}

        return self._post(
            url='{0}deployments.json'.format(self.URL),
            headers=self.headers,
            params=self.build_param_string(filters),
            data=data)

    def delete(self, application_id, id):
        """
        This API endpoint deletes the specified deployment record.
        Note: Admin User’s API Key is required.
        :type application_id: integer
        :param application_id: Application ID
        :type id: integer
        :param id: Deployment ID
        :rtype: dict
        :return: The JSON response of the API
        ::
            {
                {
                    "deployment": {
                        "id": "integer",
                        "revision": "string",
                        "changelog": "string",
                        "description": "string",
                        "user": "string",
                        "timestamp": "datetime",
                        "links": {
                            "application": "integer"
                        }
                    }
                }
        """

        return self._delete(
            url='{0}deployments/application_id={1}&id={2}.json'.format(
                self.URL, application_id, id),
            headers=self.headers)
