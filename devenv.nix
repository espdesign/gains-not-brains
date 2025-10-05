{
  pkgs,
  lib,
  config,
  ...
}: {
  # https://devenv.sh/packages/
  # packages = [
  #   # Packages for Python development
  #   config.languages.python.pkgs.flask
  # ];
  #
  # https://devenv.sh/languages/
  dotenv.enable = true;

  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = pkgs.lib.mkIf (config.languages.python.venv.enable) ''
      flask
    '';
  };

  # See full reference at https://devenv.sh/reference/options/
}
