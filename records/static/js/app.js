var app = angular.module('orto', ['angularFileUpload']);


app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

}]);


app.controller('StatusCtrl', ['$scope', '$upload', function($scope, $upload) {

    $scope.init = function(status) {
        console.log(status);
        $scope.status = status;
    }

    $scope.isActive = function(status) {
        return status == $scope.status;
    }

    $scope.setStatus = function(status) {
        $scope.status = status;
    }

}]);


app.controller('FileUploadCtrl', [
    '$scope', '$upload',
    function($scope, $upload) {

        $scope.record_id = null;
        $scope.planoDescr = '';

        $scope.plano_attachments = [];

        $scope.init = function(record_id) {
            $scope.record_id = record_id;
        }

        /*$scope.$watch('files', function () {
            $scope.upload($scope.files);
        });*/

        $scope.savePlan = function() {
            $scope.upload($scope.planoFiles, $scope.planoDescr, function(data) {
                $scope.plano_attachments.push(data.attachment);
                $scope.planoDescr = '';
            })
        }

        $scope.upload = function (files, description, cb) {

            var url = '/api/records/'+$scope.record_id+'/attachments';

            if (files && files.length) {
                for (var i = 0; i < files.length; i++) {
                    var file = files[i];
                    $upload.upload({
                        url: url,
                        fields: {'description': description},
                        file: file,
                        fileFormDataName: 'attachment',
                    }).progress(function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                    }).success(function (data, status, headers, config) {
                        console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                        cb(data);
                    });
                }
            }
        };
    }
]);
