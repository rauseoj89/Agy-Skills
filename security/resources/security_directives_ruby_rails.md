# Hardened Ruby on Rails Security Directives

When writing, generating, or auditing Ruby on Rails code, the following security standards must be strictly enforced:

### 1. Mass Assignment Protection (Strong Parameters)
Passing unvalidated parameters directly to models allows parameter pollution and field overwrites.
- **Rule:** Never use model updates directly with `params`. Require and permit parameters explicitly:
  ```ruby
  # CORRECT:
  def user_params
    params.require(:user).permit(:username, :email) # ID or Admin fields are excluded
  end
  ```

### 2. Safe Redirects
Using dynamic user params inside `redirect_to` can result in Open Redirect vulnerabilities.
- **Rule:** Restrict target scopes. Use relative paths or verify the target host:
  ```ruby
  # CORRECT:
  redirect_to safe_path_or_url(params[:next])
  ```

### Object-Level Authorization (IDOR/BOLA)
Scope ActiveRecord lookups through `current_user` (verified session/JWT) instead of global `Model.find(params[:id])`—never trust `params[:user_id]`:
```ruby
@invoice = current_user.invoices.find_by(id: params[:id])
render json: { error: "Forbidden" }, status: :forbidden and return unless @invoice
```
