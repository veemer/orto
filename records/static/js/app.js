var app = angular.module('orto', ['angularFileUpload', 'ngResource']);

// base config

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

}]);


// services

app.service('Record', ['$resource', function($resource) {
    return $resource('/api/records/:id');
}]);


// directives
app.directive('fileManager', function() {

    function controller($scope, $upload) {

        $scope.description = '';

        $scope.save = function() {

            for(var i=0; i<$scope.files.length; i++) {

                var file = $scope.files[i];

                $upload.upload({
                    url: $scope.getUrl(),
                    fields: {'description': $scope.description, 'patient_id': $scope.patient},
                    file: file,
                    fileFormDataName: 'attachment'
                }).success(function(data, status, headers, config) {

                    $scope.description = '';
                    $scope.attachments.push(data.attachment);
                    $scope.record = data.record;

                });
            }
        }

        $scope.getUrl = function() {

            var url;

            if($scope.record.id) {
                url = '/api/records/'+$scope.record.id+'/attachments';
            }
            else {
                url = '/api/records/attachments'
            }

            return url;
        }

    }

    return {
        templateUrl: '/static/partials/file-manager.html',
        controller: ['$scope', '$upload', controller],
        require: 'ngModel',
        scope: {
            record: '=',
            attachments: '=',
            patient: '=',
        }
    }

});

// controllers

app.controller('StatusCtrl', ['$scope', '$upload', function($scope, $upload) {

    $scope.init = function(status) {
        $scope.status = status;
    }

    $scope.isActive = function(status) {
        return status == $scope.status;
    }

    $scope.setStatus = function(status) {
        $scope.status = status;
    }

}]);


app.controller('RecordCtrl', [
    '$scope', '$location', 'Record',
    function($scope, $location, Record) {

        $scope.record = {}

        $scope.planogramm_attachments = []
        $scope.topogramm_attachments = []
        $scope.R_attachments = []

        $scope.save = function() {

            var params = {}

            if($scope.record.id) {
                params.id = $scope.record.id;
            }

            Record.save(params, $scope.record, function(data) {
                $scope.record.id = data.record.id;
            });
        }

        $scope.load = function(recordId) {

            if(recordId) {
                Record.get({'id': recordId}, function(data) {
                    $scope.record = data.record;
                })
            }

        }

    }
]);