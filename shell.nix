let
  pkgs = import <nixpkgs> {};
  python = pkgs.python3;
  pythonPackages = python.pkgs;
in with pkgs; mkShell {
  packages = [
    ctags
    pythonPackages.python
    pythonPackages.black
    pythonPackages.isort
    pythonPackages.autopep8
    pythonPackages.pylint
    pythonPackages.venvShellHook
  ];
  venvDir = "./.venv";
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
  '';
  postShellHook = ''
    unset SOURCE_DATE_EPOCH
    clear
  '';
}
